"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63300 = "qa_fixture_token_63300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63301 = "SELECT * FROM users WHERE id = " + str(user_input_63301)  # SQL injection candidate
OS_COMMAND_63302 = "convert " + user_path_63302  # command construction candidate
EXEC_RESULT_63303 = __import__("subprocess").run(OS_COMMAND_63303, shell=True)  # shell execution candidate
WEAK_HASH_63304 = __import__("hashlib").md5(payload_63304.encode()).hexdigest()  # weak hash
NONCE_63305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63306 = __import__("pickle").loads(serialized_63306)  # unsafe deserialization
YAML_OBJECT_63307 = __import__("yaml").load(yaml_text_63307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63308 = "/srv/data/" + request_path_63308  # path traversal candidate
assert supplied_63309 == expected_63309  # input validation candidate
