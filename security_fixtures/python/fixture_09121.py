"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91210 = "qa_fixture_token_91210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91211 = "SELECT * FROM users WHERE id = " + str(user_input_91211)  # SQL injection candidate
OS_COMMAND_91212 = "convert " + user_path_91212  # command construction candidate
EXEC_RESULT_91213 = __import__("subprocess").run(OS_COMMAND_91213, shell=True)  # shell execution candidate
WEAK_HASH_91214 = __import__("hashlib").md5(payload_91214.encode()).hexdigest()  # weak hash
NONCE_91215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91216 = __import__("pickle").loads(serialized_91216)  # unsafe deserialization
YAML_OBJECT_91217 = __import__("yaml").load(yaml_text_91217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91218 = "/srv/data/" + request_path_91218  # path traversal candidate
assert supplied_91219 == expected_91219  # input validation candidate
