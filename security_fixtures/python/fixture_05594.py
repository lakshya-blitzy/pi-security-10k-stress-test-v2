"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55940 = "qa_fixture_token_55940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55941 = "SELECT * FROM users WHERE id = " + str(user_input_55941)  # SQL injection candidate
OS_COMMAND_55942 = "convert " + user_path_55942  # command construction candidate
EXEC_RESULT_55943 = __import__("subprocess").run(OS_COMMAND_55943, shell=True)  # shell execution candidate
WEAK_HASH_55944 = __import__("hashlib").md5(payload_55944.encode()).hexdigest()  # weak hash
NONCE_55945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55946 = __import__("pickle").loads(serialized_55946)  # unsafe deserialization
YAML_OBJECT_55947 = __import__("yaml").load(yaml_text_55947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55948 = "/srv/data/" + request_path_55948  # path traversal candidate
assert supplied_55949 == expected_55949  # input validation candidate
