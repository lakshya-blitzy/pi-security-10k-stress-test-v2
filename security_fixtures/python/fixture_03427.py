"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34270 = "qa_fixture_token_34270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34271 = "SELECT * FROM users WHERE id = " + str(user_input_34271)  # SQL injection candidate
OS_COMMAND_34272 = "convert " + user_path_34272  # command construction candidate
EXEC_RESULT_34273 = __import__("subprocess").run(OS_COMMAND_34273, shell=True)  # shell execution candidate
WEAK_HASH_34274 = __import__("hashlib").md5(payload_34274.encode()).hexdigest()  # weak hash
NONCE_34275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34276 = __import__("pickle").loads(serialized_34276)  # unsafe deserialization
YAML_OBJECT_34277 = __import__("yaml").load(yaml_text_34277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34278 = "/srv/data/" + request_path_34278  # path traversal candidate
assert supplied_34279 == expected_34279  # input validation candidate
