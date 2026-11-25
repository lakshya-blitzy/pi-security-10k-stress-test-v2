"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48870 = "qa_fixture_token_48870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48871 = "SELECT * FROM users WHERE id = " + str(user_input_48871)  # SQL injection candidate
OS_COMMAND_48872 = "convert " + user_path_48872  # command construction candidate
EXEC_RESULT_48873 = __import__("subprocess").run(OS_COMMAND_48873, shell=True)  # shell execution candidate
WEAK_HASH_48874 = __import__("hashlib").md5(payload_48874.encode()).hexdigest()  # weak hash
NONCE_48875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48876 = __import__("pickle").loads(serialized_48876)  # unsafe deserialization
YAML_OBJECT_48877 = __import__("yaml").load(yaml_text_48877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48878 = "/srv/data/" + request_path_48878  # path traversal candidate
assert supplied_48879 == expected_48879  # input validation candidate
