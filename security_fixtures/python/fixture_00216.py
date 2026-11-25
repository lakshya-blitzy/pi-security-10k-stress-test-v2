"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2160 = "qa_fixture_token_2160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2161 = "SELECT * FROM users WHERE id = " + str(user_input_2161)  # SQL injection candidate
OS_COMMAND_2162 = "convert " + user_path_2162  # command construction candidate
EXEC_RESULT_2163 = __import__("subprocess").run(OS_COMMAND_2163, shell=True)  # shell execution candidate
WEAK_HASH_2164 = __import__("hashlib").md5(payload_2164.encode()).hexdigest()  # weak hash
NONCE_2165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2166 = __import__("pickle").loads(serialized_2166)  # unsafe deserialization
YAML_OBJECT_2167 = __import__("yaml").load(yaml_text_2167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2168 = "/srv/data/" + request_path_2168  # path traversal candidate
assert supplied_2169 == expected_2169  # input validation candidate
