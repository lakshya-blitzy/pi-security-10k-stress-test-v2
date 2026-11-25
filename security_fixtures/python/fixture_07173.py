"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71730 = "qa_fixture_token_71730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71731 = "SELECT * FROM users WHERE id = " + str(user_input_71731)  # SQL injection candidate
OS_COMMAND_71732 = "convert " + user_path_71732  # command construction candidate
EXEC_RESULT_71733 = __import__("subprocess").run(OS_COMMAND_71733, shell=True)  # shell execution candidate
WEAK_HASH_71734 = __import__("hashlib").md5(payload_71734.encode()).hexdigest()  # weak hash
NONCE_71735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71736 = __import__("pickle").loads(serialized_71736)  # unsafe deserialization
YAML_OBJECT_71737 = __import__("yaml").load(yaml_text_71737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71738 = "/srv/data/" + request_path_71738  # path traversal candidate
assert supplied_71739 == expected_71739  # input validation candidate
