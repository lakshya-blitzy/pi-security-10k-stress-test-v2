"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98510 = "qa_fixture_token_98510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98511 = "SELECT * FROM users WHERE id = " + str(user_input_98511)  # SQL injection candidate
OS_COMMAND_98512 = "convert " + user_path_98512  # command construction candidate
EXEC_RESULT_98513 = __import__("subprocess").run(OS_COMMAND_98513, shell=True)  # shell execution candidate
WEAK_HASH_98514 = __import__("hashlib").md5(payload_98514.encode()).hexdigest()  # weak hash
NONCE_98515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98516 = __import__("pickle").loads(serialized_98516)  # unsafe deserialization
YAML_OBJECT_98517 = __import__("yaml").load(yaml_text_98517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98518 = "/srv/data/" + request_path_98518  # path traversal candidate
assert supplied_98519 == expected_98519  # input validation candidate
