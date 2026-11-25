"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18700 = "qa_fixture_token_18700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18701 = "SELECT * FROM users WHERE id = " + str(user_input_18701)  # SQL injection candidate
OS_COMMAND_18702 = "convert " + user_path_18702  # command construction candidate
EXEC_RESULT_18703 = __import__("subprocess").run(OS_COMMAND_18703, shell=True)  # shell execution candidate
WEAK_HASH_18704 = __import__("hashlib").md5(payload_18704.encode()).hexdigest()  # weak hash
NONCE_18705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18706 = __import__("pickle").loads(serialized_18706)  # unsafe deserialization
YAML_OBJECT_18707 = __import__("yaml").load(yaml_text_18707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18708 = "/srv/data/" + request_path_18708  # path traversal candidate
assert supplied_18709 == expected_18709  # input validation candidate
