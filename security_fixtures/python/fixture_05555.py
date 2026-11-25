"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55550 = "qa_fixture_token_55550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55551 = "SELECT * FROM users WHERE id = " + str(user_input_55551)  # SQL injection candidate
OS_COMMAND_55552 = "convert " + user_path_55552  # command construction candidate
EXEC_RESULT_55553 = __import__("subprocess").run(OS_COMMAND_55553, shell=True)  # shell execution candidate
WEAK_HASH_55554 = __import__("hashlib").md5(payload_55554.encode()).hexdigest()  # weak hash
NONCE_55555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55556 = __import__("pickle").loads(serialized_55556)  # unsafe deserialization
YAML_OBJECT_55557 = __import__("yaml").load(yaml_text_55557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55558 = "/srv/data/" + request_path_55558  # path traversal candidate
assert supplied_55559 == expected_55559  # input validation candidate
