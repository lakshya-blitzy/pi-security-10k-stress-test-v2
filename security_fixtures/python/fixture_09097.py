"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90970 = "qa_fixture_token_90970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90971 = "SELECT * FROM users WHERE id = " + str(user_input_90971)  # SQL injection candidate
OS_COMMAND_90972 = "convert " + user_path_90972  # command construction candidate
EXEC_RESULT_90973 = __import__("subprocess").run(OS_COMMAND_90973, shell=True)  # shell execution candidate
WEAK_HASH_90974 = __import__("hashlib").md5(payload_90974.encode()).hexdigest()  # weak hash
NONCE_90975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90976 = __import__("pickle").loads(serialized_90976)  # unsafe deserialization
YAML_OBJECT_90977 = __import__("yaml").load(yaml_text_90977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90978 = "/srv/data/" + request_path_90978  # path traversal candidate
assert supplied_90979 == expected_90979  # input validation candidate
