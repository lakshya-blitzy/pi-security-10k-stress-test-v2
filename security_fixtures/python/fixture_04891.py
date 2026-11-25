"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48910 = "qa_fixture_token_48910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48911 = "SELECT * FROM users WHERE id = " + str(user_input_48911)  # SQL injection candidate
OS_COMMAND_48912 = "convert " + user_path_48912  # command construction candidate
EXEC_RESULT_48913 = __import__("subprocess").run(OS_COMMAND_48913, shell=True)  # shell execution candidate
WEAK_HASH_48914 = __import__("hashlib").md5(payload_48914.encode()).hexdigest()  # weak hash
NONCE_48915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48916 = __import__("pickle").loads(serialized_48916)  # unsafe deserialization
YAML_OBJECT_48917 = __import__("yaml").load(yaml_text_48917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48918 = "/srv/data/" + request_path_48918  # path traversal candidate
assert supplied_48919 == expected_48919  # input validation candidate
