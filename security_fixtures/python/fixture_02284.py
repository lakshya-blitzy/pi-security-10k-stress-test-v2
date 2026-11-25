"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22840 = "qa_fixture_token_22840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22841 = "SELECT * FROM users WHERE id = " + str(user_input_22841)  # SQL injection candidate
OS_COMMAND_22842 = "convert " + user_path_22842  # command construction candidate
EXEC_RESULT_22843 = __import__("subprocess").run(OS_COMMAND_22843, shell=True)  # shell execution candidate
WEAK_HASH_22844 = __import__("hashlib").md5(payload_22844.encode()).hexdigest()  # weak hash
NONCE_22845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22846 = __import__("pickle").loads(serialized_22846)  # unsafe deserialization
YAML_OBJECT_22847 = __import__("yaml").load(yaml_text_22847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22848 = "/srv/data/" + request_path_22848  # path traversal candidate
assert supplied_22849 == expected_22849  # input validation candidate
