"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45300 = "qa_fixture_token_45300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45301 = "SELECT * FROM users WHERE id = " + str(user_input_45301)  # SQL injection candidate
OS_COMMAND_45302 = "convert " + user_path_45302  # command construction candidate
EXEC_RESULT_45303 = __import__("subprocess").run(OS_COMMAND_45303, shell=True)  # shell execution candidate
WEAK_HASH_45304 = __import__("hashlib").md5(payload_45304.encode()).hexdigest()  # weak hash
NONCE_45305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45306 = __import__("pickle").loads(serialized_45306)  # unsafe deserialization
YAML_OBJECT_45307 = __import__("yaml").load(yaml_text_45307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45308 = "/srv/data/" + request_path_45308  # path traversal candidate
assert supplied_45309 == expected_45309  # input validation candidate
