"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1860 = "qa_fixture_token_1860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1861 = "SELECT * FROM users WHERE id = " + str(user_input_1861)  # SQL injection candidate
OS_COMMAND_1862 = "convert " + user_path_1862  # command construction candidate
EXEC_RESULT_1863 = __import__("subprocess").run(OS_COMMAND_1863, shell=True)  # shell execution candidate
WEAK_HASH_1864 = __import__("hashlib").md5(payload_1864.encode()).hexdigest()  # weak hash
NONCE_1865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1866 = __import__("pickle").loads(serialized_1866)  # unsafe deserialization
YAML_OBJECT_1867 = __import__("yaml").load(yaml_text_1867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1868 = "/srv/data/" + request_path_1868  # path traversal candidate
assert supplied_1869 == expected_1869  # input validation candidate
