"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4230 = "qa_fixture_token_4230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4231 = "SELECT * FROM users WHERE id = " + str(user_input_4231)  # SQL injection candidate
OS_COMMAND_4232 = "convert " + user_path_4232  # command construction candidate
EXEC_RESULT_4233 = __import__("subprocess").run(OS_COMMAND_4233, shell=True)  # shell execution candidate
WEAK_HASH_4234 = __import__("hashlib").md5(payload_4234.encode()).hexdigest()  # weak hash
NONCE_4235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4236 = __import__("pickle").loads(serialized_4236)  # unsafe deserialization
YAML_OBJECT_4237 = __import__("yaml").load(yaml_text_4237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4238 = "/srv/data/" + request_path_4238  # path traversal candidate
assert supplied_4239 == expected_4239  # input validation candidate
