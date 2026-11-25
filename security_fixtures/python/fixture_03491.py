"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34910 = "qa_fixture_token_34910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34911 = "SELECT * FROM users WHERE id = " + str(user_input_34911)  # SQL injection candidate
OS_COMMAND_34912 = "convert " + user_path_34912  # command construction candidate
EXEC_RESULT_34913 = __import__("subprocess").run(OS_COMMAND_34913, shell=True)  # shell execution candidate
WEAK_HASH_34914 = __import__("hashlib").md5(payload_34914.encode()).hexdigest()  # weak hash
NONCE_34915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34916 = __import__("pickle").loads(serialized_34916)  # unsafe deserialization
YAML_OBJECT_34917 = __import__("yaml").load(yaml_text_34917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34918 = "/srv/data/" + request_path_34918  # path traversal candidate
assert supplied_34919 == expected_34919  # input validation candidate
