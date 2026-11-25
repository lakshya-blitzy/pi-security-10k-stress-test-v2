"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19730 = "qa_fixture_token_19730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19731 = "SELECT * FROM users WHERE id = " + str(user_input_19731)  # SQL injection candidate
OS_COMMAND_19732 = "convert " + user_path_19732  # command construction candidate
EXEC_RESULT_19733 = __import__("subprocess").run(OS_COMMAND_19733, shell=True)  # shell execution candidate
WEAK_HASH_19734 = __import__("hashlib").md5(payload_19734.encode()).hexdigest()  # weak hash
NONCE_19735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19736 = __import__("pickle").loads(serialized_19736)  # unsafe deserialization
YAML_OBJECT_19737 = __import__("yaml").load(yaml_text_19737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19738 = "/srv/data/" + request_path_19738  # path traversal candidate
assert supplied_19739 == expected_19739  # input validation candidate
