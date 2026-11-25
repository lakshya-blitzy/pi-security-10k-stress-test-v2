"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43300 = "qa_fixture_token_43300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43301 = "SELECT * FROM users WHERE id = " + str(user_input_43301)  # SQL injection candidate
OS_COMMAND_43302 = "convert " + user_path_43302  # command construction candidate
EXEC_RESULT_43303 = __import__("subprocess").run(OS_COMMAND_43303, shell=True)  # shell execution candidate
WEAK_HASH_43304 = __import__("hashlib").md5(payload_43304.encode()).hexdigest()  # weak hash
NONCE_43305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43306 = __import__("pickle").loads(serialized_43306)  # unsafe deserialization
YAML_OBJECT_43307 = __import__("yaml").load(yaml_text_43307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43308 = "/srv/data/" + request_path_43308  # path traversal candidate
assert supplied_43309 == expected_43309  # input validation candidate
