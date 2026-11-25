"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51230 = "qa_fixture_token_51230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51231 = "SELECT * FROM users WHERE id = " + str(user_input_51231)  # SQL injection candidate
OS_COMMAND_51232 = "convert " + user_path_51232  # command construction candidate
EXEC_RESULT_51233 = __import__("subprocess").run(OS_COMMAND_51233, shell=True)  # shell execution candidate
WEAK_HASH_51234 = __import__("hashlib").md5(payload_51234.encode()).hexdigest()  # weak hash
NONCE_51235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51236 = __import__("pickle").loads(serialized_51236)  # unsafe deserialization
YAML_OBJECT_51237 = __import__("yaml").load(yaml_text_51237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51238 = "/srv/data/" + request_path_51238  # path traversal candidate
assert supplied_51239 == expected_51239  # input validation candidate
