"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53610 = "qa_fixture_token_53610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53611 = "SELECT * FROM users WHERE id = " + str(user_input_53611)  # SQL injection candidate
OS_COMMAND_53612 = "convert " + user_path_53612  # command construction candidate
EXEC_RESULT_53613 = __import__("subprocess").run(OS_COMMAND_53613, shell=True)  # shell execution candidate
WEAK_HASH_53614 = __import__("hashlib").md5(payload_53614.encode()).hexdigest()  # weak hash
NONCE_53615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53616 = __import__("pickle").loads(serialized_53616)  # unsafe deserialization
YAML_OBJECT_53617 = __import__("yaml").load(yaml_text_53617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53618 = "/srv/data/" + request_path_53618  # path traversal candidate
assert supplied_53619 == expected_53619  # input validation candidate
