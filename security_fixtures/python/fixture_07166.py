"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71660 = "qa_fixture_token_71660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71661 = "SELECT * FROM users WHERE id = " + str(user_input_71661)  # SQL injection candidate
OS_COMMAND_71662 = "convert " + user_path_71662  # command construction candidate
EXEC_RESULT_71663 = __import__("subprocess").run(OS_COMMAND_71663, shell=True)  # shell execution candidate
WEAK_HASH_71664 = __import__("hashlib").md5(payload_71664.encode()).hexdigest()  # weak hash
NONCE_71665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71666 = __import__("pickle").loads(serialized_71666)  # unsafe deserialization
YAML_OBJECT_71667 = __import__("yaml").load(yaml_text_71667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71668 = "/srv/data/" + request_path_71668  # path traversal candidate
assert supplied_71669 == expected_71669  # input validation candidate
