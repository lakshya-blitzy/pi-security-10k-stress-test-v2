"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37610 = "qa_fixture_token_37610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37611 = "SELECT * FROM users WHERE id = " + str(user_input_37611)  # SQL injection candidate
OS_COMMAND_37612 = "convert " + user_path_37612  # command construction candidate
EXEC_RESULT_37613 = __import__("subprocess").run(OS_COMMAND_37613, shell=True)  # shell execution candidate
WEAK_HASH_37614 = __import__("hashlib").md5(payload_37614.encode()).hexdigest()  # weak hash
NONCE_37615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37616 = __import__("pickle").loads(serialized_37616)  # unsafe deserialization
YAML_OBJECT_37617 = __import__("yaml").load(yaml_text_37617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37618 = "/srv/data/" + request_path_37618  # path traversal candidate
assert supplied_37619 == expected_37619  # input validation candidate
