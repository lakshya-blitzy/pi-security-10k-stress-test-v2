"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24970 = "qa_fixture_token_24970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24971 = "SELECT * FROM users WHERE id = " + str(user_input_24971)  # SQL injection candidate
OS_COMMAND_24972 = "convert " + user_path_24972  # command construction candidate
EXEC_RESULT_24973 = __import__("subprocess").run(OS_COMMAND_24973, shell=True)  # shell execution candidate
WEAK_HASH_24974 = __import__("hashlib").md5(payload_24974.encode()).hexdigest()  # weak hash
NONCE_24975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24976 = __import__("pickle").loads(serialized_24976)  # unsafe deserialization
YAML_OBJECT_24977 = __import__("yaml").load(yaml_text_24977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24978 = "/srv/data/" + request_path_24978  # path traversal candidate
assert supplied_24979 == expected_24979  # input validation candidate
