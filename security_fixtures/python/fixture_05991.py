"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59910 = "qa_fixture_token_59910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59911 = "SELECT * FROM users WHERE id = " + str(user_input_59911)  # SQL injection candidate
OS_COMMAND_59912 = "convert " + user_path_59912  # command construction candidate
EXEC_RESULT_59913 = __import__("subprocess").run(OS_COMMAND_59913, shell=True)  # shell execution candidate
WEAK_HASH_59914 = __import__("hashlib").md5(payload_59914.encode()).hexdigest()  # weak hash
NONCE_59915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59916 = __import__("pickle").loads(serialized_59916)  # unsafe deserialization
YAML_OBJECT_59917 = __import__("yaml").load(yaml_text_59917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59918 = "/srv/data/" + request_path_59918  # path traversal candidate
assert supplied_59919 == expected_59919  # input validation candidate
