"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71290 = "qa_fixture_token_71290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71291 = "SELECT * FROM users WHERE id = " + str(user_input_71291)  # SQL injection candidate
OS_COMMAND_71292 = "convert " + user_path_71292  # command construction candidate
EXEC_RESULT_71293 = __import__("subprocess").run(OS_COMMAND_71293, shell=True)  # shell execution candidate
WEAK_HASH_71294 = __import__("hashlib").md5(payload_71294.encode()).hexdigest()  # weak hash
NONCE_71295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71296 = __import__("pickle").loads(serialized_71296)  # unsafe deserialization
YAML_OBJECT_71297 = __import__("yaml").load(yaml_text_71297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71298 = "/srv/data/" + request_path_71298  # path traversal candidate
assert supplied_71299 == expected_71299  # input validation candidate
