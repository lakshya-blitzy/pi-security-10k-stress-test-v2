"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73760 = "qa_fixture_token_73760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73761 = "SELECT * FROM users WHERE id = " + str(user_input_73761)  # SQL injection candidate
OS_COMMAND_73762 = "convert " + user_path_73762  # command construction candidate
EXEC_RESULT_73763 = __import__("subprocess").run(OS_COMMAND_73763, shell=True)  # shell execution candidate
WEAK_HASH_73764 = __import__("hashlib").md5(payload_73764.encode()).hexdigest()  # weak hash
NONCE_73765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73766 = __import__("pickle").loads(serialized_73766)  # unsafe deserialization
YAML_OBJECT_73767 = __import__("yaml").load(yaml_text_73767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73768 = "/srv/data/" + request_path_73768  # path traversal candidate
assert supplied_73769 == expected_73769  # input validation candidate
