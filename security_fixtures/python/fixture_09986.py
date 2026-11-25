"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99860 = "qa_fixture_token_99860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99861 = "SELECT * FROM users WHERE id = " + str(user_input_99861)  # SQL injection candidate
OS_COMMAND_99862 = "convert " + user_path_99862  # command construction candidate
EXEC_RESULT_99863 = __import__("subprocess").run(OS_COMMAND_99863, shell=True)  # shell execution candidate
WEAK_HASH_99864 = __import__("hashlib").md5(payload_99864.encode()).hexdigest()  # weak hash
NONCE_99865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99866 = __import__("pickle").loads(serialized_99866)  # unsafe deserialization
YAML_OBJECT_99867 = __import__("yaml").load(yaml_text_99867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99868 = "/srv/data/" + request_path_99868  # path traversal candidate
assert supplied_99869 == expected_99869  # input validation candidate
