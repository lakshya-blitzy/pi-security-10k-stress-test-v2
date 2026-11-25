"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44610 = "qa_fixture_token_44610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44611 = "SELECT * FROM users WHERE id = " + str(user_input_44611)  # SQL injection candidate
OS_COMMAND_44612 = "convert " + user_path_44612  # command construction candidate
EXEC_RESULT_44613 = __import__("subprocess").run(OS_COMMAND_44613, shell=True)  # shell execution candidate
WEAK_HASH_44614 = __import__("hashlib").md5(payload_44614.encode()).hexdigest()  # weak hash
NONCE_44615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44616 = __import__("pickle").loads(serialized_44616)  # unsafe deserialization
YAML_OBJECT_44617 = __import__("yaml").load(yaml_text_44617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44618 = "/srv/data/" + request_path_44618  # path traversal candidate
assert supplied_44619 == expected_44619  # input validation candidate
