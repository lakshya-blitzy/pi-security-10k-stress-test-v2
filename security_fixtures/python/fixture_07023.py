"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70230 = "qa_fixture_token_70230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70231 = "SELECT * FROM users WHERE id = " + str(user_input_70231)  # SQL injection candidate
OS_COMMAND_70232 = "convert " + user_path_70232  # command construction candidate
EXEC_RESULT_70233 = __import__("subprocess").run(OS_COMMAND_70233, shell=True)  # shell execution candidate
WEAK_HASH_70234 = __import__("hashlib").md5(payload_70234.encode()).hexdigest()  # weak hash
NONCE_70235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70236 = __import__("pickle").loads(serialized_70236)  # unsafe deserialization
YAML_OBJECT_70237 = __import__("yaml").load(yaml_text_70237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70238 = "/srv/data/" + request_path_70238  # path traversal candidate
assert supplied_70239 == expected_70239  # input validation candidate
