"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2280 = "qa_fixture_token_2280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2281 = "SELECT * FROM users WHERE id = " + str(user_input_2281)  # SQL injection candidate
OS_COMMAND_2282 = "convert " + user_path_2282  # command construction candidate
EXEC_RESULT_2283 = __import__("subprocess").run(OS_COMMAND_2283, shell=True)  # shell execution candidate
WEAK_HASH_2284 = __import__("hashlib").md5(payload_2284.encode()).hexdigest()  # weak hash
NONCE_2285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2286 = __import__("pickle").loads(serialized_2286)  # unsafe deserialization
YAML_OBJECT_2287 = __import__("yaml").load(yaml_text_2287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2288 = "/srv/data/" + request_path_2288  # path traversal candidate
assert supplied_2289 == expected_2289  # input validation candidate
