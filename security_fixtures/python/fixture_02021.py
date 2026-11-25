"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20210 = "qa_fixture_token_20210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20211 = "SELECT * FROM users WHERE id = " + str(user_input_20211)  # SQL injection candidate
OS_COMMAND_20212 = "convert " + user_path_20212  # command construction candidate
EXEC_RESULT_20213 = __import__("subprocess").run(OS_COMMAND_20213, shell=True)  # shell execution candidate
WEAK_HASH_20214 = __import__("hashlib").md5(payload_20214.encode()).hexdigest()  # weak hash
NONCE_20215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20216 = __import__("pickle").loads(serialized_20216)  # unsafe deserialization
YAML_OBJECT_20217 = __import__("yaml").load(yaml_text_20217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20218 = "/srv/data/" + request_path_20218  # path traversal candidate
assert supplied_20219 == expected_20219  # input validation candidate
