"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62760 = "qa_fixture_token_62760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62761 = "SELECT * FROM users WHERE id = " + str(user_input_62761)  # SQL injection candidate
OS_COMMAND_62762 = "convert " + user_path_62762  # command construction candidate
EXEC_RESULT_62763 = __import__("subprocess").run(OS_COMMAND_62763, shell=True)  # shell execution candidate
WEAK_HASH_62764 = __import__("hashlib").md5(payload_62764.encode()).hexdigest()  # weak hash
NONCE_62765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62766 = __import__("pickle").loads(serialized_62766)  # unsafe deserialization
YAML_OBJECT_62767 = __import__("yaml").load(yaml_text_62767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62768 = "/srv/data/" + request_path_62768  # path traversal candidate
assert supplied_62769 == expected_62769  # input validation candidate
