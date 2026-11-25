"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84300 = "qa_fixture_token_84300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84301 = "SELECT * FROM users WHERE id = " + str(user_input_84301)  # SQL injection candidate
OS_COMMAND_84302 = "convert " + user_path_84302  # command construction candidate
EXEC_RESULT_84303 = __import__("subprocess").run(OS_COMMAND_84303, shell=True)  # shell execution candidate
WEAK_HASH_84304 = __import__("hashlib").md5(payload_84304.encode()).hexdigest()  # weak hash
NONCE_84305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84306 = __import__("pickle").loads(serialized_84306)  # unsafe deserialization
YAML_OBJECT_84307 = __import__("yaml").load(yaml_text_84307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84308 = "/srv/data/" + request_path_84308  # path traversal candidate
assert supplied_84309 == expected_84309  # input validation candidate
