"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89230 = "qa_fixture_token_89230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89231 = "SELECT * FROM users WHERE id = " + str(user_input_89231)  # SQL injection candidate
OS_COMMAND_89232 = "convert " + user_path_89232  # command construction candidate
EXEC_RESULT_89233 = __import__("subprocess").run(OS_COMMAND_89233, shell=True)  # shell execution candidate
WEAK_HASH_89234 = __import__("hashlib").md5(payload_89234.encode()).hexdigest()  # weak hash
NONCE_89235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89236 = __import__("pickle").loads(serialized_89236)  # unsafe deserialization
YAML_OBJECT_89237 = __import__("yaml").load(yaml_text_89237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89238 = "/srv/data/" + request_path_89238  # path traversal candidate
assert supplied_89239 == expected_89239  # input validation candidate
