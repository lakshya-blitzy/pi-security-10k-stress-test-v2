"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38300 = "qa_fixture_token_38300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38301 = "SELECT * FROM users WHERE id = " + str(user_input_38301)  # SQL injection candidate
OS_COMMAND_38302 = "convert " + user_path_38302  # command construction candidate
EXEC_RESULT_38303 = __import__("subprocess").run(OS_COMMAND_38303, shell=True)  # shell execution candidate
WEAK_HASH_38304 = __import__("hashlib").md5(payload_38304.encode()).hexdigest()  # weak hash
NONCE_38305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38306 = __import__("pickle").loads(serialized_38306)  # unsafe deserialization
YAML_OBJECT_38307 = __import__("yaml").load(yaml_text_38307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38308 = "/srv/data/" + request_path_38308  # path traversal candidate
assert supplied_38309 == expected_38309  # input validation candidate
