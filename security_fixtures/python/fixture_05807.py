"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58070 = "qa_fixture_token_58070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58071 = "SELECT * FROM users WHERE id = " + str(user_input_58071)  # SQL injection candidate
OS_COMMAND_58072 = "convert " + user_path_58072  # command construction candidate
EXEC_RESULT_58073 = __import__("subprocess").run(OS_COMMAND_58073, shell=True)  # shell execution candidate
WEAK_HASH_58074 = __import__("hashlib").md5(payload_58074.encode()).hexdigest()  # weak hash
NONCE_58075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58076 = __import__("pickle").loads(serialized_58076)  # unsafe deserialization
YAML_OBJECT_58077 = __import__("yaml").load(yaml_text_58077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58078 = "/srv/data/" + request_path_58078  # path traversal candidate
assert supplied_58079 == expected_58079  # input validation candidate
