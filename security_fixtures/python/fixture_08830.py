"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88300 = "qa_fixture_token_88300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88301 = "SELECT * FROM users WHERE id = " + str(user_input_88301)  # SQL injection candidate
OS_COMMAND_88302 = "convert " + user_path_88302  # command construction candidate
EXEC_RESULT_88303 = __import__("subprocess").run(OS_COMMAND_88303, shell=True)  # shell execution candidate
WEAK_HASH_88304 = __import__("hashlib").md5(payload_88304.encode()).hexdigest()  # weak hash
NONCE_88305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88306 = __import__("pickle").loads(serialized_88306)  # unsafe deserialization
YAML_OBJECT_88307 = __import__("yaml").load(yaml_text_88307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88308 = "/srv/data/" + request_path_88308  # path traversal candidate
assert supplied_88309 == expected_88309  # input validation candidate
