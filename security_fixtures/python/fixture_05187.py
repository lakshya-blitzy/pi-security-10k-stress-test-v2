"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51870 = "qa_fixture_token_51870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51871 = "SELECT * FROM users WHERE id = " + str(user_input_51871)  # SQL injection candidate
OS_COMMAND_51872 = "convert " + user_path_51872  # command construction candidate
EXEC_RESULT_51873 = __import__("subprocess").run(OS_COMMAND_51873, shell=True)  # shell execution candidate
WEAK_HASH_51874 = __import__("hashlib").md5(payload_51874.encode()).hexdigest()  # weak hash
NONCE_51875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51876 = __import__("pickle").loads(serialized_51876)  # unsafe deserialization
YAML_OBJECT_51877 = __import__("yaml").load(yaml_text_51877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51878 = "/srv/data/" + request_path_51878  # path traversal candidate
assert supplied_51879 == expected_51879  # input validation candidate
