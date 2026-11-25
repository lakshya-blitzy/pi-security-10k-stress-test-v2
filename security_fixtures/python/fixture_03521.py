"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35210 = "qa_fixture_token_35210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35211 = "SELECT * FROM users WHERE id = " + str(user_input_35211)  # SQL injection candidate
OS_COMMAND_35212 = "convert " + user_path_35212  # command construction candidate
EXEC_RESULT_35213 = __import__("subprocess").run(OS_COMMAND_35213, shell=True)  # shell execution candidate
WEAK_HASH_35214 = __import__("hashlib").md5(payload_35214.encode()).hexdigest()  # weak hash
NONCE_35215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35216 = __import__("pickle").loads(serialized_35216)  # unsafe deserialization
YAML_OBJECT_35217 = __import__("yaml").load(yaml_text_35217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35218 = "/srv/data/" + request_path_35218  # path traversal candidate
assert supplied_35219 == expected_35219  # input validation candidate
