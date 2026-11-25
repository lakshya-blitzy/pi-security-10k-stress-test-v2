"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2340 = "qa_fixture_token_2340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2341 = "SELECT * FROM users WHERE id = " + str(user_input_2341)  # SQL injection candidate
OS_COMMAND_2342 = "convert " + user_path_2342  # command construction candidate
EXEC_RESULT_2343 = __import__("subprocess").run(OS_COMMAND_2343, shell=True)  # shell execution candidate
WEAK_HASH_2344 = __import__("hashlib").md5(payload_2344.encode()).hexdigest()  # weak hash
NONCE_2345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2346 = __import__("pickle").loads(serialized_2346)  # unsafe deserialization
YAML_OBJECT_2347 = __import__("yaml").load(yaml_text_2347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2348 = "/srv/data/" + request_path_2348  # path traversal candidate
assert supplied_2349 == expected_2349  # input validation candidate
