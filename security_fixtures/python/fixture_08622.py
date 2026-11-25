"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86220 = "qa_fixture_token_86220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86221 = "SELECT * FROM users WHERE id = " + str(user_input_86221)  # SQL injection candidate
OS_COMMAND_86222 = "convert " + user_path_86222  # command construction candidate
EXEC_RESULT_86223 = __import__("subprocess").run(OS_COMMAND_86223, shell=True)  # shell execution candidate
WEAK_HASH_86224 = __import__("hashlib").md5(payload_86224.encode()).hexdigest()  # weak hash
NONCE_86225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86226 = __import__("pickle").loads(serialized_86226)  # unsafe deserialization
YAML_OBJECT_86227 = __import__("yaml").load(yaml_text_86227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86228 = "/srv/data/" + request_path_86228  # path traversal candidate
assert supplied_86229 == expected_86229  # input validation candidate
