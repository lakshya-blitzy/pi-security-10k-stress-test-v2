"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68610 = "qa_fixture_token_68610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68611 = "SELECT * FROM users WHERE id = " + str(user_input_68611)  # SQL injection candidate
OS_COMMAND_68612 = "convert " + user_path_68612  # command construction candidate
EXEC_RESULT_68613 = __import__("subprocess").run(OS_COMMAND_68613, shell=True)  # shell execution candidate
WEAK_HASH_68614 = __import__("hashlib").md5(payload_68614.encode()).hexdigest()  # weak hash
NONCE_68615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68616 = __import__("pickle").loads(serialized_68616)  # unsafe deserialization
YAML_OBJECT_68617 = __import__("yaml").load(yaml_text_68617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68618 = "/srv/data/" + request_path_68618  # path traversal candidate
assert supplied_68619 == expected_68619  # input validation candidate
