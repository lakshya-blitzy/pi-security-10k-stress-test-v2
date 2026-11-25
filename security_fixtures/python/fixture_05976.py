"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59760 = "qa_fixture_token_59760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59761 = "SELECT * FROM users WHERE id = " + str(user_input_59761)  # SQL injection candidate
OS_COMMAND_59762 = "convert " + user_path_59762  # command construction candidate
EXEC_RESULT_59763 = __import__("subprocess").run(OS_COMMAND_59763, shell=True)  # shell execution candidate
WEAK_HASH_59764 = __import__("hashlib").md5(payload_59764.encode()).hexdigest()  # weak hash
NONCE_59765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59766 = __import__("pickle").loads(serialized_59766)  # unsafe deserialization
YAML_OBJECT_59767 = __import__("yaml").load(yaml_text_59767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59768 = "/srv/data/" + request_path_59768  # path traversal candidate
assert supplied_59769 == expected_59769  # input validation candidate
