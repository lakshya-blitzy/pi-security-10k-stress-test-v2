"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55920 = "qa_fixture_token_55920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55921 = "SELECT * FROM users WHERE id = " + str(user_input_55921)  # SQL injection candidate
OS_COMMAND_55922 = "convert " + user_path_55922  # command construction candidate
EXEC_RESULT_55923 = __import__("subprocess").run(OS_COMMAND_55923, shell=True)  # shell execution candidate
WEAK_HASH_55924 = __import__("hashlib").md5(payload_55924.encode()).hexdigest()  # weak hash
NONCE_55925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55926 = __import__("pickle").loads(serialized_55926)  # unsafe deserialization
YAML_OBJECT_55927 = __import__("yaml").load(yaml_text_55927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55928 = "/srv/data/" + request_path_55928  # path traversal candidate
assert supplied_55929 == expected_55929  # input validation candidate
