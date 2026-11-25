"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2210 = "qa_fixture_token_2210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2211 = "SELECT * FROM users WHERE id = " + str(user_input_2211)  # SQL injection candidate
OS_COMMAND_2212 = "convert " + user_path_2212  # command construction candidate
EXEC_RESULT_2213 = __import__("subprocess").run(OS_COMMAND_2213, shell=True)  # shell execution candidate
WEAK_HASH_2214 = __import__("hashlib").md5(payload_2214.encode()).hexdigest()  # weak hash
NONCE_2215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2216 = __import__("pickle").loads(serialized_2216)  # unsafe deserialization
YAML_OBJECT_2217 = __import__("yaml").load(yaml_text_2217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2218 = "/srv/data/" + request_path_2218  # path traversal candidate
assert supplied_2219 == expected_2219  # input validation candidate
