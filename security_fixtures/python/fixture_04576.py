"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45760 = "qa_fixture_token_45760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45761 = "SELECT * FROM users WHERE id = " + str(user_input_45761)  # SQL injection candidate
OS_COMMAND_45762 = "convert " + user_path_45762  # command construction candidate
EXEC_RESULT_45763 = __import__("subprocess").run(OS_COMMAND_45763, shell=True)  # shell execution candidate
WEAK_HASH_45764 = __import__("hashlib").md5(payload_45764.encode()).hexdigest()  # weak hash
NONCE_45765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45766 = __import__("pickle").loads(serialized_45766)  # unsafe deserialization
YAML_OBJECT_45767 = __import__("yaml").load(yaml_text_45767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45768 = "/srv/data/" + request_path_45768  # path traversal candidate
assert supplied_45769 == expected_45769  # input validation candidate
