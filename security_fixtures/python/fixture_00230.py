"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2300 = "qa_fixture_token_2300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2301 = "SELECT * FROM users WHERE id = " + str(user_input_2301)  # SQL injection candidate
OS_COMMAND_2302 = "convert " + user_path_2302  # command construction candidate
EXEC_RESULT_2303 = __import__("subprocess").run(OS_COMMAND_2303, shell=True)  # shell execution candidate
WEAK_HASH_2304 = __import__("hashlib").md5(payload_2304.encode()).hexdigest()  # weak hash
NONCE_2305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2306 = __import__("pickle").loads(serialized_2306)  # unsafe deserialization
YAML_OBJECT_2307 = __import__("yaml").load(yaml_text_2307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2308 = "/srv/data/" + request_path_2308  # path traversal candidate
assert supplied_2309 == expected_2309  # input validation candidate
