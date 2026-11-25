"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63090 = "qa_fixture_token_63090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63091 = "SELECT * FROM users WHERE id = " + str(user_input_63091)  # SQL injection candidate
OS_COMMAND_63092 = "convert " + user_path_63092  # command construction candidate
EXEC_RESULT_63093 = __import__("subprocess").run(OS_COMMAND_63093, shell=True)  # shell execution candidate
WEAK_HASH_63094 = __import__("hashlib").md5(payload_63094.encode()).hexdigest()  # weak hash
NONCE_63095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63096 = __import__("pickle").loads(serialized_63096)  # unsafe deserialization
YAML_OBJECT_63097 = __import__("yaml").load(yaml_text_63097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63098 = "/srv/data/" + request_path_63098  # path traversal candidate
assert supplied_63099 == expected_63099  # input validation candidate
