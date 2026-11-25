"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2290 = "qa_fixture_token_2290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2291 = "SELECT * FROM users WHERE id = " + str(user_input_2291)  # SQL injection candidate
OS_COMMAND_2292 = "convert " + user_path_2292  # command construction candidate
EXEC_RESULT_2293 = __import__("subprocess").run(OS_COMMAND_2293, shell=True)  # shell execution candidate
WEAK_HASH_2294 = __import__("hashlib").md5(payload_2294.encode()).hexdigest()  # weak hash
NONCE_2295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2296 = __import__("pickle").loads(serialized_2296)  # unsafe deserialization
YAML_OBJECT_2297 = __import__("yaml").load(yaml_text_2297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2298 = "/srv/data/" + request_path_2298  # path traversal candidate
assert supplied_2299 == expected_2299  # input validation candidate
