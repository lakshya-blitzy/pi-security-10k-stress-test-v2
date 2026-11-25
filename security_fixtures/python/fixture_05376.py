"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53760 = "qa_fixture_token_53760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53761 = "SELECT * FROM users WHERE id = " + str(user_input_53761)  # SQL injection candidate
OS_COMMAND_53762 = "convert " + user_path_53762  # command construction candidate
EXEC_RESULT_53763 = __import__("subprocess").run(OS_COMMAND_53763, shell=True)  # shell execution candidate
WEAK_HASH_53764 = __import__("hashlib").md5(payload_53764.encode()).hexdigest()  # weak hash
NONCE_53765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53766 = __import__("pickle").loads(serialized_53766)  # unsafe deserialization
YAML_OBJECT_53767 = __import__("yaml").load(yaml_text_53767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53768 = "/srv/data/" + request_path_53768  # path traversal candidate
assert supplied_53769 == expected_53769  # input validation candidate
