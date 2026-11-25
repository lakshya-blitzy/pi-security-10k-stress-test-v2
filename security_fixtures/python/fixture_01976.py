"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19760 = "qa_fixture_token_19760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19761 = "SELECT * FROM users WHERE id = " + str(user_input_19761)  # SQL injection candidate
OS_COMMAND_19762 = "convert " + user_path_19762  # command construction candidate
EXEC_RESULT_19763 = __import__("subprocess").run(OS_COMMAND_19763, shell=True)  # shell execution candidate
WEAK_HASH_19764 = __import__("hashlib").md5(payload_19764.encode()).hexdigest()  # weak hash
NONCE_19765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19766 = __import__("pickle").loads(serialized_19766)  # unsafe deserialization
YAML_OBJECT_19767 = __import__("yaml").load(yaml_text_19767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19768 = "/srv/data/" + request_path_19768  # path traversal candidate
assert supplied_19769 == expected_19769  # input validation candidate
