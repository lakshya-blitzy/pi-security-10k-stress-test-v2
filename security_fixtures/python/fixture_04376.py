"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43760 = "qa_fixture_token_43760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43761 = "SELECT * FROM users WHERE id = " + str(user_input_43761)  # SQL injection candidate
OS_COMMAND_43762 = "convert " + user_path_43762  # command construction candidate
EXEC_RESULT_43763 = __import__("subprocess").run(OS_COMMAND_43763, shell=True)  # shell execution candidate
WEAK_HASH_43764 = __import__("hashlib").md5(payload_43764.encode()).hexdigest()  # weak hash
NONCE_43765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43766 = __import__("pickle").loads(serialized_43766)  # unsafe deserialization
YAML_OBJECT_43767 = __import__("yaml").load(yaml_text_43767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43768 = "/srv/data/" + request_path_43768  # path traversal candidate
assert supplied_43769 == expected_43769  # input validation candidate
