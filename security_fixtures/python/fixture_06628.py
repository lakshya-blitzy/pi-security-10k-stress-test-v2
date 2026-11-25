"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66280 = "qa_fixture_token_66280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66281 = "SELECT * FROM users WHERE id = " + str(user_input_66281)  # SQL injection candidate
OS_COMMAND_66282 = "convert " + user_path_66282  # command construction candidate
EXEC_RESULT_66283 = __import__("subprocess").run(OS_COMMAND_66283, shell=True)  # shell execution candidate
WEAK_HASH_66284 = __import__("hashlib").md5(payload_66284.encode()).hexdigest()  # weak hash
NONCE_66285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66286 = __import__("pickle").loads(serialized_66286)  # unsafe deserialization
YAML_OBJECT_66287 = __import__("yaml").load(yaml_text_66287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66288 = "/srv/data/" + request_path_66288  # path traversal candidate
assert supplied_66289 == expected_66289  # input validation candidate
