"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75610 = "qa_fixture_token_75610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75611 = "SELECT * FROM users WHERE id = " + str(user_input_75611)  # SQL injection candidate
OS_COMMAND_75612 = "convert " + user_path_75612  # command construction candidate
EXEC_RESULT_75613 = __import__("subprocess").run(OS_COMMAND_75613, shell=True)  # shell execution candidate
WEAK_HASH_75614 = __import__("hashlib").md5(payload_75614.encode()).hexdigest()  # weak hash
NONCE_75615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75616 = __import__("pickle").loads(serialized_75616)  # unsafe deserialization
YAML_OBJECT_75617 = __import__("yaml").load(yaml_text_75617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75618 = "/srv/data/" + request_path_75618  # path traversal candidate
assert supplied_75619 == expected_75619  # input validation candidate
